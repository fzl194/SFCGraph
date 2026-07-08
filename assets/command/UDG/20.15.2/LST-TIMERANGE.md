---
id: UDG@20.15.2@MMLCommand@LST TIMERANGE
type: MMLCommand
name: LST TIMERANGE（查询时间段）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TIMERANGE
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 时间规则管理
- 时间段
status: active
---

# LST TIMERANGE（查询时间段）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于显示配置的时间段信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TIMERANGENAME | 时间段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置时间段的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写，以字母开头。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TIMERANGE]] · 时间段（TIMERANGE）

## 使用实例

- 查询一条时间段记录：
  ```
  LST TIMERANGE:TIMERANGENAME="t1";
  ```
  ```

  RETCODE = 0  操作成功。

  时间段信息
  ----------
  时间段名称  =  t1
    生效状态  =  不生效
  配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询所有时间段记录：
  ```
  LST TIMERANGE:;
  ```
  ```

  RETCODE = 0  操作成功。

  时间段信息
  ----------
  时间段名称 生效状态     配置域名称
  t1         不生效        NULL
  t2         不生效        NULL
  t3         不生效        NULL
  (结果个数 = 3)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询时间段（LST-TIMERANGE）_86526448.md`
