---
id: UNC@20.15.2@MMLCommand@ADD TLSPSKGRP
type: MMLCommand
name: ADD TLSPSKGRP（增加TLS预共享密钥组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: TLSPSKGRP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP TLS预共享密钥组管理
status: active
---

# ADD TLSPSKGRP（增加TLS预共享密钥组）

## 功能

该命令用于增加预共享密钥组。

当需要建立HTTPS链路且使用预共享密钥方式进行认证时，可通过此命令添加预共享密钥组，用于关联一个或多个预共享密钥。

客户端发起建链时会随机选择组内某一个预共享密钥，并在TLS建链消息中携带预共享密钥标识。服务端从TLS建链消息中提取预共享密钥标识，匹配组内预共享密钥标识，获取对应的预共享密钥进行建链协商。

当需要平滑替换某个预共享密钥，可先后在服务端和客户端通过命令 [**ADD TLSPSK**](../HTTP TLS预共享密钥管理/增加预共享密钥（ADD TLSPSK）_07669721.md) 在同一组内添加新的预共享密钥信息，然后先后在客户端和服务端执行 [**RMV TLSPSK**](../HTTP TLS预共享密钥管理/删除预共享密钥（RMV TLSPSK）_57029816.md) 命令删除不再使用的预共享密钥信息，保证业务无损。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入128条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PSKGRPIDX | 预共享密钥组索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TLS预共享密钥组的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TLS预共享密钥组的描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TLSPSKGRP]] · 预共享密钥组信息（TLSPSKGRP）

## 使用实例

若需要添加一个预共享密钥组，组索引为1，可以执行如下命令：

```
ADD TLSPSKGRP: PSKGRPIDX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加TLS预共享密钥组（ADD-TLSPSKGRP）_07789673.md`
