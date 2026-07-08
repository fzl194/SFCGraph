---
id: UDG@20.15.2@MMLCommand@SET FOOLPROOFSWITCH
type: MMLCommand
name: SET FOOLPROOFSWITCH（设置防呆开关状态）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: FOOLPROOFSWITCH
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 一键式部署
status: active
---

# SET FOOLPROOFSWITCH（设置防呆开关状态）

## 功能

该命令用于设置防呆开关状态。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | 名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示防呆开关名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无。<br>配置原则：无 |
| STATUS | 状态 | 可选必选说明：可选参数<br>参数含义：该参数用于表示防呆开关状态。<br>数据来源：本端规划<br>取值范围：<br>- “ON（打开）”：防呆开关打开<br>- “OFF（关闭）”：防呆开关关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST FOOLPROOFSWITCH查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FOOLPROOFSWITCH]] · 防呆开关状态（FOOLPROOFSWITCH）

## 使用实例

假如运营商由于上次一键式部署任务失败且任务无法恢复成功，导致无法下发其他一键式部署任务。调用以下命令可以关闭防呆开关，成功下发其他一键式部署任务。

```
%%SET FOOLPROOFSWITCH: NAME="ONECLICKDEPLOY", STATUS=OFF;%%
RETCODE = 0  操作成功

结果如下
--------
名称  =  ONECLICKDEPLOY
状态  =  关闭
结果  =  set ONECLICKDEPLOY to OFF success
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-FOOLPROOFSWITCH.md`
