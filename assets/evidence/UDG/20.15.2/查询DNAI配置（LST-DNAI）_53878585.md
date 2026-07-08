# 查询DNAI配置（LST DNAI）

- [命令功能](#ZH-CN_CONCEPT_0253878585__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0253878585__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0253878585__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0253878585__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0253878585__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0253878585__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0253878585)

**适用NF：PGW-U、UPF**

该命令用来查看指定DNAI实例或者已配置所有DNAI实例的配置信息。

#### [注意事项](#ZH-CN_CONCEPT_0253878585)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0253878585)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0253878585)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNAI | 数据网络接入标识 | 可选必选说明：可选参数<br>参数含义：数据网络接入标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。名称中不能包含空格，不区分大小写。<br>默认值：无<br>配置原则：输入的DNAI名称需要符合DNAI命名规则。 |

#### [使用实例](#ZH-CN_CONCEPT_0253878585)

- 显示指定DNAI实例的信息：
  ```
  LST DNAI:DNAI="huawei01.com";
  ```
  ```

  %%LST DNAI: DNAI="huawei01.com";%%
  RETCODE = 0  操作成功

  DNAI信息
  --------
  数据网络接入标识  =  huawei01.com
           绑定VPN  =  使能
         VPN实例名  =  vpn01
      绑定IPv6 VPN  =  不使能
    IPv6 VPN实例名  =  NULL
       NAT功能开关  =  使能
          锁定  =  不使能
  (结果个数 = 1)

  ---    END
  ```
- 查询整机DNAI实例信息：
  ```
  LST DNAI:;
  ```
  ```

  %%LST DNAI:;%%
  RETCODE = 0  操作成功

  DNAI信息
  --------
  数据网络接入标识  绑定VPN  VPN实例名  绑定IPv6 VPN  IPv6 VPN实例名  NAT功能开关  锁定

  huawei01.com      使能     vpn01      不使能        NULL            使能         不使能
  huawei02.com      使能     vpn02      不使能        NULL            使能         不使能
  huawei03.com      使能     vpn03      不使能        NULL            不使能       不使能
  (结果个数 = 3)

  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0253878585)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 锁定 | 用于配置DNAI进行锁定操作。 |

其余输出项请参见ADD DNAI的参数说明。
