---
id: UDG@20.15.2@MMLCommand@LST AUTOSCALINGRUBLACKLIST
type: MMLCommand
name: LST AUTOSCALINGRUBLACKLIST（查询自动部署RU黑名单）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: AUTOSCALINGRUBLACKLIST
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- 自动化配置RU黑名单
status: active
---

# LST AUTOSCALINGRUBLACKLIST（查询自动部署RU黑名单）

## 功能

该命令用于查询自动化配置RU黑名单。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUID | RU ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定RU ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～9999。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@AUTOSCALINGRUBLACKLIST]] · 自动部署RU黑名单（AUTOSCALINGRUBLACKLIST）

## 使用实例

查询自动化配置RU黑名单：

```
LST AUTOSCALINGRUBLACKLIST:;
```

```
RETCODE = 0 操作成功

结果如下
-------------------------
RU ID

64
65
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-AUTOSCALINGRUBLACKLIST.md`
