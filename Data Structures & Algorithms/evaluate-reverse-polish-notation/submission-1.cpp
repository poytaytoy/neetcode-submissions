#include <span> 
#include <string>

bool is_symbol(std::string& symbol){
    if (symbol == "*"){
        return true; 
    } else if (symbol == "/"){
        return true; 
    } else if (symbol == "+"){
        return true; 
    } else if (symbol == "-"){ 
        return true; 
    } else { 
        return false; 
    }
}

struct Expression { 
    virtual int evaluate() = 0; 
    virtual ~Expression() = default;
};

struct Number: public Expression { 
    int i; 
    
    Number(int i): i {i} {}
    
    int evaluate() override {
        return i; 
    }
};

struct Operation: public Expression { 
    std::string symbol; 
    std::shared_ptr<Expression> exp1; 
    std::shared_ptr<Expression> exp2;

    Operation(std::string& symbol, std::shared_ptr<Expression> exp1, std::shared_ptr<Expression> exp2): symbol{symbol}, exp1{exp1}, exp2{exp2}{}

    int evaluate() override { 
        int n1 = exp1->evaluate(); 
        int n2 = exp2->evaluate(); 

        if (symbol == "*"){
            return n1 * n2; 
        } else if (symbol == "/"){
            return n1 / n2; 
        } else if (symbol == "+"){
            return n1 + n2; 
        } else { 
            return n1 - n2; 
        }
    }
};

std::pair<std::shared_ptr<Expression>, std::span<string>> parse(std::span<string> token){
    if (is_symbol(token[token.size() - 1])){
        std::string symbol = token[token.size() - 1]; 
        
        auto [exp1, token1] = parse(token.first(token.size() - 1)); 
        auto [exp2, token2] = parse(token1);

        return {
            std::make_shared<Operation>(symbol, exp2, exp1), 
            token2 
        };

    } else { 
        return {
            std::make_shared<Number>(std::stoi(token[token.size() - 1])), 
            token.first(token.size() - 1)
        };
    }
}

class Solution {
public:

    int evalRPN(vector<string>& tokens) {

        auto result = parse(std::span<string>(tokens));

        return result.first->evaluate(); 
    }
};
