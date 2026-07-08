---
id: UDG@20.15.2@MMLCommand@ADD ACLDEFAULT
type: MMLCommand
name: ADD ACLDEFAULT（增加缺省Acl绑定）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: ACLDEFAULT
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 4
category_path:
- 用户面服务管理
- 业务安全防护
- 用户ACL管理
- 缺省ACL绑定
status: active
---

# ADD ACLDEFAULT（增加缺省Acl绑定）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于增加默认的ACL。默认ACL是在APN下没有配置任何ACL时，如果APN需要使用ACL，则会使用默认ACL。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为4。
- 区分down-link in-bound、down-link out-bound、up-link in-bound、up-link out-bound四个方向的绑定。如果默认ACL下绑定的节点中动作不符合要求，则返回失败；如果默认ACL下未绑定ACL节点，则不做检查。
- 首先需要将ACL节点绑定到ACL之后，再添加默认的ACL。如果先添加默认的ACL，再将ACL节点绑定到该默认的ACL，如果绑定的ACL节点的动作类型与默认ACL的方向冲突，则不会提示该错误，并且匹配到默认ACL规则的报文会按照PASS处理。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DIRECTION | 方向 | 可选必选说明：必选参数<br>参数含义：该参数用于指定默认ACL的方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- UPIN：APN绑定ACL的方向为上行进系统。<br>- UPOUT：APN绑定ACL的方向为上行出系统。<br>- DOWNIN：APN绑定ACL的方向为下行进系统。<br>- DOWNOUT：APN绑定ACL的方向为下行出系统。<br>默认值：无<br>配置原则：按实际需要控制的方向来置值。 |
| ACLNAME | ACL名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置默认ACL名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD ACL命令配置生成。<br>- 当参数Direction配置为UPIN、DOWNIN时，该参数只能配置ACL节点的动作为gate、remark的ACL名称。<br>- 当参数Direction配置为UPOUT、DOWNOUT时，该参数只能配置ACL节点的动作为redirect的ACL名称。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ACLDEFAULT]] · 缺省Acl绑定（ACLDEFAULT）

## 使用实例

假如运营商需要在上行、进系统方向增加一个名称为“testacl1”的默认ACL：

```
ADD ACLDEFAULT:DIRECTION=UPIN,ACLNAME="testacl1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-ACLDEFAULT.md`
