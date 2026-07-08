---
id: UDG@20.15.2@MMLCommand@LST USERPROFILE
type: MMLCommand
name: LST USERPROFILE（查询用户模板）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: USERPROFILE
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务规则管理
- 用户模板
status: active
---

# LST USERPROFILE（查询用户模板）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询用户模板。

## 注意事项

如果不输入用户模板名称，表示查询系统中所有用户模板。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及“,”、“;”、“"”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| UPSPECTYPE | 用户模板规格类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户模板类型，当取值为SPECIFICATION_LIMITED时，表示规格受限用户模板，表示会话安装的该类型的USERPROFILE数和该类型的USERPROFILE绑定的规则数量均存在一定限制。<br>数据来源：本端规划<br>取值范围：<br>- DEFAULT：默认配置。<br>- SPECIFICATION_LIMITED：规格受限配置。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [用户模板（USERPROFILE）](configobject/UDG/20.15.2/USERPROFILE.md)

## 使用实例

- 假如运营商需要查询名称为testuserprofile1的用户模板：
  ```
  LST USERPROFILE: USERPROFILENAME="testuserprofile1";
  ```
  ```

  RETCODE = 0  操作成功。

  用户模板信息
  ------------
                             用户模板名称  =  testuserprofile1
                         用户模板规格类型  =  默认配置
                    Alias Marking使能标记  =  不使能
                           防DDOS攻击标记  =  不使能
                Captive模式时间阈值（分）  =  0
                   配额申请时报文处理动作  =  缓存
                         实时位置上报开关  =  继承
                                 锁定标记  =  不使能
                            缺省URR组名称  =  NULL
                        缺省信令URR组名称  =  NULL
                          重定向URR组名称  =  NULL
                          TCP重传计费标识  =  未配置
                         TCP重传URR组名称  =  NULL
                            URL白名单名称  =  NULL
                             扩展属性名称  =  NULL
                    CCR-Initia URR组名称1  =  NULL
                   CCR-Initial URR组名称2  =  NULL
                   CCR-Initial URR组名称3  =  NULL
                   CCR-Initial URR组名称4  =  NULL
                   CCR-Initial URR组名称5  =  NULL
                   CCR-Initial URR组名称6  =  NULL
                   CCR-Initial URR组名称7  =  NULL
                   CCR-Initial URR组名称8  =  NULL
                   CCR-Initial URR组名称9  =  NULL
                  CCR-Initial URR组名称10  =  NULL
                             用户模板别名  =  NULL
                 IPv6 TCP报文长度（字节）  =  0
                 IPv4 TCP报文长度（字节）  =  0
  Tethering用户下最多可接入后台终端的数量  =  0
                               配置域名称  =  NULL
                继承全局缺省URR组配置开关  =  使能
                继承全局缺省信令URR组开关  =  使能
  (结果个数 = 1)
  ---    END
  ```
- 假如运营商需要查询所有的用户模板：
  ```
  LST USERPROFILE:;
  ```
  ```

  RETCODE = 0  操作成功。

  用户模板信息
  ------------
  用户模板名称        用户模板规格类型        Alias Marking使能标记    防DDOS攻击标记    Captive模式时间阈值（分）    配额申请时报文处理动作    实时位置上报开关    锁定标记    缺省URR组名称    缺省信令URR组名称    重定向URR组名称    TCP重传计费标识    TCP重传URR组名称    URL白名单名称    扩展属性名称    CCR-Initia URR组名称1    CCR-Initial URR组名称2    CCR-Initial URR组名称3    CCR-Initial URR组名称4    CCR-Initial URR组名称5    CCR-Initial URR组名称6    CCR-Initial URR组名称7    CCR-Initial URR组名称8    CCR-Initial URR组名称9    CCR-Initial URR组名称10    用户模板别名    IPv6 TCP报文长度（字节）    IPv4 TCP报文长度（字节）    Tethering用户下最多可接入后台终端的数量    配置域名称  继承全局缺省URR组配置开关  继承全局缺省信令URR组开关

  testuserprofile1    默认配置        不使能                   不使能            0                            缓存                      继承                不使能      NULL             NULL                 NULL               未配置             NULL                NULL             NULL            NULL                     NULL                      NULL                      NULL                      NULL                      NULL                      NULL                      NULL                      NULL                      NULL                       NULL            0                           0                           0                                          NULL               使能               使能
  testuserprofile2    默认配置        不使能                   不使能            0                            缓存                      继承                不使能      NULL             NULL                 NULL               未配置             NULL                NULL             NULL            NULL                     NULL                      NULL                      NULL                      NULL                      NULL                      NULL                      NULL                      NULL                      NULL                       NULL            0                           0                           0                                          NULL               使能               使能
  testuserprofile3    默认配置        不使能                   不使能            0                            缓存                      继承                不使能      NULL             NULL                 NULL               未配置             NULL                NULL             NULL            NULL                     NULL                      NULL                      NULL                      NULL                      NULL                      NULL                      NULL                      NULL                      NULL                       NULL            0                           0                           0                                          NULL               使能               使能
  (结果个数 = 3)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询用户模板（LST-USERPROFILE）_82837286.md`
