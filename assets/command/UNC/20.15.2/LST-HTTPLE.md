---
id: UNC@20.15.2@MMLCommand@LST HTTPLE
type: MMLCommand
name: LST HTTPLE（查询HTTP本端实体）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTTPLE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP本端实体管理
status: active
---

# LST HTTPLE（查询HTTP本端实体）

## 功能

该命令用于查询HTTP本端实体配置信息。

## 注意事项

- 仅指定HTTP本端实体索引时，查询某一HTTP本端实体配置信息。
- 仅指定HTTP本端实体组标识时， 查询该实体组标识下的所有HTTP本端实体信息。
- 仅指定本端实体类型时，查询所有本端实体类型为客户端或服务端的HTTP本端实体配置信息。
- 指定HTTP本端实体组标识和本端实体类型时查询该实体组下的客户端配置或服务端配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | HTTPLE本端实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTTP本端实体的索引信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| HTTPLEGRPIDX | HTTP本端实体组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTTP本端实体所属的HTTP本端实体组。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~64。<br>默认值：无<br>配置原则：<br>执行本命令前，需要先确认HTTPLEGRPIDX已经通过<br>[**ADD HTTPLEGRP**](../HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md)<br>添加。 |
| LETYPE | 本端实体类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTTP本端实体的类型。<br>数据来源：全网规划<br>取值范围：<br>- “SERVER（服务端）”：服务端<br>- “CLIENT（客户端）”：客户端<br>默认值：无<br>配置原则：<br>HTTP本端实体可以作为服务端也可以作为客户端，两者需要分别配置。 |

## 操作的配置对象

- [HTTP本端实体（HTTPLE）](configobject/UNC/20.15.2/HTTPLE.md)

## 使用实例

- 若运营商想查询索引为1的HTTP本端实体配置信息，可以用如下命令；
  ```
  %%LST HTTPLE: INDEX=1;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
        HTTPLE本端实体索引  =  1
        HTTP本端实体组标识  =  1
              本端实体类型  =  SERVER
                    端口号  =  30110
               是否启用TLS  =  NO
                    TLS索引  =  0
                       描述  =  NULL
                     IP类型  =  IPv6
                   IPv4地址  =  0.0.0.0
                   IPv6地址  =  2001:0db8::84:2:145:10
                    VPN名称  =  _public_
                    路由标记 = 否
  (结果个数 = 1)

  ---    END
  ```
- 若运营商想查询所有的HTTP本端实体配置信息，可以用如下命令；
  ```
  %%LST HTTPLE:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
        HTTPLE本端实体索引  =  1
        HTTP本端实体组标识  =  1
              本端实体类型  =  SERVER
                    端口号  =  30110
               是否启用TLS  =  NO
                    TLS索引  =  0
                       描述  =  NULL
                     IP类型  =  IPv6
                   IPv4地址  =  0.0.0.0
                   IPv6地址  =  2001:0db8::84:2:145:10
                    VPN名称  =  _public_
                    路由标记 = 否
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询HTTP本端实体（LST-HTTPLE）_29291769.md`
