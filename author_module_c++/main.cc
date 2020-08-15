#include <iostream>
#include "authorized_check.h"

int main(int argc, char* argv[]) {
    AuthorizedCheck ac;
    int32_t res = 0;
    // "172.17.170.205" 为远程服务端ip
    ac.init(std::string("172.17.170.205"), 8080);
    // 构造请求，填充token，目前不进行token校验，随便填一个string即可
    ac.gen_request("token_test");
    // 执行鉴权判断
    res = ac.run_check();
    if (res == 0) {
        std::cout << "author failed, exit!!" << std::endl;
    } else if (res == 1) {
        std::cout << "author success, easy mode" << std::endl;
    } else if (res == 2) {
        std::cout << "author success, middle mode" << std::endl;
    } else if (res == 3) {
        std::cout << "author success, hard mode" << std::endl;
    } else {
        std::cout << "FATAL!! unexpected result!!" << std::endl;
    }
}
