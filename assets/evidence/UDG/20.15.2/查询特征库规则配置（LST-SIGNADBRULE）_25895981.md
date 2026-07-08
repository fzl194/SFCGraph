# 查询特征库规则配置（LST SIGNADBRULE）

- [命令功能](#ZH-CN_CONCEPT_0225895981__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0225895981__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0225895981__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0225895981__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0225895981__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0225895981__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0225895981)

**适用NF：PGW-U、UPF**

该命令用于查询特征库中应用协议、应用子协议的动态识别规则。

#### [注意事项](#ZH-CN_CONCEPT_0225895981)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0225895981)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0225895981)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SIGNADBRULENAME | 特征库规则协议名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置特征库规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0225895981)

- 假如运营商想要查询名称为test_sigrule的动态识别规则：
  ```
  LST SIGNADBRULE:SIGNADBRULENAME="test_signadbrule";
  ```
  ```

  RETCODE = 0  操作成功。

  特征库规则信息
  --------------
  特征库规则协议名称  =  test_signadbrule
            协议名称  =  facebook_others
      IP地址配置模式  =  IP
        Host配置名称  =  NULL
      IP地址版本类型  =  IPV4
            IPv4地址  =  10.0.0.1
            IPv6地址  =  ::
          IP地址掩码  =  16
          端口操作码  =  NULL
    服务器起始端口号  =  0
    服务器结束端口号  =  0
              优先级  =  0
  (结果个数 = 1)
  ---    END
  ```
- 假如运营商想要查询所有应用子协议的动态识别规则：
  ```
  LST SIGNADBRULE:;
  ```
  ```

  RETCODE = 0  操作成功。

  特征库规则信息
  --------------
  特征库规则协议名称    协议名称           IP地址配置模式    Host配置名称    IP地址版本类型    IPv4地址    IPv6地址    IP地址掩码    端口操作码    服务器起始端口号    服务器结束端口号    优先级

  test2                  facebook_others    IP                NULL            IPV4              10.0.0.2    ::          1             NULL          0                   0                   0     
  test_signadbrule       facebook_others    IP                NULL            IPV4              10.0.0.1    ::          16            NULL          0                   0                   0     
  (结果个数 = 2)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0225895981)

参见ADD SIGNADBRULE的参数说明。
