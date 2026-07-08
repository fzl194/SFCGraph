---
id: UDG@20.15.2@MMLCommand@LST FILTER
type: MMLCommand
name: LST FILTER（查询过滤器）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FILTER
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 流过滤器管理
- 过滤器
status: active
---

# LST FILTER（查询过滤器）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询过滤器。

## 注意事项

过滤器可以被绑定到过滤器组、流过滤器或Acl中，过滤器的Effective生效标志只用于标志该过滤器在过滤器组或流过滤器下是否生效。当过滤器被绑定在Acl中此标志无效，即无论该过滤器是否生效，Acl中的过滤器均可用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FILTERNAME | 过滤器名字 | 可选必选说明：可选参数<br>参数含义：该参数用于设置过滤器名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：如果不输入过滤器名称，表示查询系统中所有过滤器。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@FILTER]] · 过滤器（FILTER）

## 使用实例

- 运营商需要查询名称为filter1的过滤器：
  ```
  LST FILTER:FILTERNAME="filter1";
  ```
  ```

  RETCODE = 0  操作成功

  过滤器信息
  ----------
                过滤器名字  =  filter1
    三四层IPv4协议输入类型  =  字符串类型
    三四层IPv6协议输入类型  =  NULL
        三四层协议数字类型  =  0
            三四层协议类型  =  ANY
        手机IP地址配置模式  =  IP
            IP地址版本类型  =  IPV4
                手机IP地址  =  10.0.0.1
      手机IP地址掩码类型  =  反掩码地址类型
      手机IP地址掩码长度  =  0
          手机IP地址反掩码  =  255.255.255.255
              手机IPv6地址  =  ::
    手机IPv6地址掩码类型  =  反掩码地址类型
    手机IPv6地址掩码长度  =  0
        手机IPv6地址反掩码  =  FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
            手机IP列表名称  =  NULL
      服务器IP地址配置模式  =  NULL
              服务器IP地址  =  0.0.0.0
    服务器IP地址掩码类型  =  反掩码地址类型
    服务器IP地址掩码长度  =  0
        服务器IP地址反掩码  =  255.255.255.255
            服务器IPv6地址  =  ::
  服务器IPv6地址掩码类型  =  反掩码地址类型
  服务器IPv6地址掩码长度  =  0
      服务器IPv6地址反掩码  =  FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
              Host配置名称  =  NULL
          服务器IP列表名称  =  NULL
            手机起始端口号  =  0
            手机结束端口号  =  65535
          服务器起始端口号  =  0
          服务器结束端口号  =  65535
               Tos配置类型  =  NULL
               Tos分类类型  =  NULL
                  服务类型  =  NULL
                  生效标记  =  否
                配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 运营商需要查询所有的过滤器：
  ```
  LST FILTER:;
  ```
  ```

  RETCODE = 0  操作成功

  过滤器信息
  ----------
  过滤器名字  三四层IPv4协议输入类型  三四层IPv6协议输入类型  三四层协议数字类型  三四层协议类型  手机IP地址配置模式  IP地址版本类型  手机IP地址  手机IP地址掩码类型  手机IP地址掩码长度  手机IP地址反掩码  手机IPv6地址  手机IPv6地址掩码类型  手机IPv6地址掩码长度  手机IPv6地址反掩码                       手机IP列表名称  服务器IP地址配置模式  服务器IP地址  服务器IP地址掩码类型  服务器IP地址掩码长度  服务器IP地址反掩码  服务器IPv6地址  服务器IPv6地址掩码类型  服务器IPv6地址掩码长度  服务器IPv6地址反掩码                     Host配置名称  服务器IP列表名称  手机起始端口号  手机结束端口号  服务器起始端口号  服务器结束端口号  Tos配置类型  Tos分类类型  服务类型  生效标记  配置域名称  

  filter1     字符串类型              NULL                    0                   ANY             IP                  IPV4            10.0.0.1    反掩码地址类型        0                     255.255.255.255   ::            反掩码地址类型          0                       FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF  NULL            NULL                  0.0.0.0       反掩码地址类型          0                       255.255.255.255     ::              反掩码地址类型            0                         FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF  NULL          NULL              0               65535           0                 65535             NULL         NULL         NULL      否        NULL        
  filter2     NULL                    字符串类型              6                   TCP             IP                  IPV6            0.0.0.0     反掩码地址类型        0                     255.255.255.255   fc00::1         反掩码地址类型          0                       FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF  NULL            NULL                  0.0.0.0       反掩码地址类型          0                       255.255.255.255     ::              反掩码地址类型            0                         FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF  NULL          NULL              0               65535           0                 65535             NULL         NULL         NULL      否        NULL        
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-FILTER.md`
