---
id: UNC@20.15.2@MMLCommand@MOD APPLYTUNNELPOLICY
type: MMLCommand
name: MOD APPLYTUNNELPOLICY（修改应用隧道策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: APPLYTUNNELPOLICY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 隧道选择器管理
- 应用隧道策略
status: active
---

# MOD APPLYTUNNELPOLICY（修改应用隧道策略）

## 功能

该命令用来修改应用隧道策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNLSELECTORNAME | 隧道选择器名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定隧道选择器名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～40。<br>默认值：无 |
| NODESEQUENCE | 隧道选择器节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定隧道选择器节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| TNLPOLICYNAME | 隧道策略名 | 可选必选说明：必选参数<br>参数含义：该参数用于表示隧道策略名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～39。<br>默认值：无 |

## 操作的配置对象

- [应用隧道策略（APPLYTUNNELPOLICY）](configobject/UNC/20.15.2/APPLYTUNNELPOLICY.md)

## 使用实例

修改应用隧道策略的操作：

```
MOD APPLYTUNNELPOLICY:TNLSELECTORNAME="a",NODESEQUENCE=10,TNLPOLICYNAME="b";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改应用隧道策略（MOD-APPLYTUNNELPOLICY）_00440317.md`
