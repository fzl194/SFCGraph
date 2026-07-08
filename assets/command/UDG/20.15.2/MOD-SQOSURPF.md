---
id: UDG@20.15.2@MMLCommand@MOD SQOSURPF
type: MMLCommand
name: MOD SQOSURPF（修改流行为安全URPF）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: SQOSURPF
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 流行为安全URPF
status: active
---

# MOD SQOSURPF（修改流行为安全URPF）

## 功能

该命令用来修改流行为下的URPF（单播反向路由转发）配置。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEHAVIORNAME | 流行为名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流行为名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| URPFTYPE | URPF检查类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定安全URPF增强型检查。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- strict：严格检查：不但要求在转发表中存在相应表项，还要求接口一定匹配才能通过URPF检查。<br>- loose：松散检查：只要在转发表中存在表项就通过URPF检查，不要求接口一定匹配。<br>默认值：无 |
| URPFDEFAULT | 匹配默认路由 | 可选必选说明：必选参数<br>参数含义：该参数用于指定默认安全URPF。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- disallow：不接受。<br>- allow：接受。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SQOSURPF]] · 流行为安全URPF（SQOSURPF）

## 使用实例

修改流行为下的安全URPF配置：

```
MOD SQOSURPF:BEHAVIORNAME="b1",URPFTYPE=loose,URPFDEFAULT=allow;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-SQOSURPF.md`
