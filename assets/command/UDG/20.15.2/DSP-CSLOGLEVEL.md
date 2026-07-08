---
id: UDG@20.15.2@MMLCommand@DSP CSLOGLEVEL
type: MMLCommand
name: DSP CSLOGLEVEL（查询日志级别）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: CSLOGLEVEL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 日志管理
status: active
---

# DSP CSLOGLEVEL（查询日志级别）

## 功能

此命令用于查询日志级别。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 进程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示进程类型。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| CELLID | 进程标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示进程标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CSLOGLEVEL]] · 更新日志输出级别（CSLOGLEVEL）

## 使用实例

查询日志级别：

```
%%DSP CSLOGLEVEL: CELLTYPE=110, CELLID="haf-pod-d69365cc-vk4c5192-168-0-134__108__0";%%
RETCODE = 0  操作成功

结果如下
--------
进程类型  =  110
进程标识  =  haf-pod-d69365cc-vk4c5192-168-0-134__108__0
日志级别  =  调试级别
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-CSLOGLEVEL.md`
