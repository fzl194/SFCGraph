---
id: UDG@20.15.2@MMLCommand@MOD WKRFLAGEASSOSW
type: MMLCommand
name: MOD WKRFLAGEASSOSW（修改Worker流表老化关联开关）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: WKRFLAGEASSOSW
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务五元组管理
- Worker五元组老化关联开关
status: active
---

# MOD WKRFLAGEASSOSW（修改Worker流表老化关联开关）

## 功能

**适用NF：UPF**

该命令用于更新特定类型Worker的流表老化关联功能开关。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WORKERNAME | Worker名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置需要控制流表关联老化功能的Worker名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：根据部署的业务策略选择相应的子策略名称。选择范围和ADD RULE的WORKERNAME一致。 |
| SWITCH | 开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置是否开启流表关联老化功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@WKRFLAGEASSOSW]] · Worker流表老化关联开关（WKRFLAGEASSOSW）

## 使用实例

当需要修改to的流表老化关联功能为开启时，进行如下设置：

```
MOD WKRFLAGEASSOSW: WORKERNAME="to", SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-WKRFLAGEASSOSW.md`
