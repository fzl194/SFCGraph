---
id: UDG@20.15.2@MMLCommand@LST ABSTIMERANGE
type: MMLCommand
name: LST ABSTIMERANGE（查询绝对时间段）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ABSTIMERANGE
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
- 绝对时间段
status: active
---

# LST ABSTIMERANGE（查询绝对时间段）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于显示配置的绝对时间段信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TIMERANGENAME | 时间段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置时间段的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写，以字母开头。<br>默认值：无<br>配置原则：无 |
| ABSTIMERANGESEQ | 绝对时间段序号 | 可选必选说明：可选参数<br>参数含义：该参数用于设置绝对时间段的序号值。在一个时间段内，绝对时间段序号不能重复，每一个序号代表一个绝对时间段。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～12。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ABSTIMERANGE]] · 绝对时间段（ABSTIMERANGE）

## 使用实例

- 查询一条绝对时间段记录：
  ```
  LST ABSTIMERANGE:TIMERANGENAME="t1",ABSTIMERANGESEQ=1;
  ```
  ```

  RETCODE = 0  操作成功。

  绝对时间段信息
  --------------
                时间段名称  =  t1
            绝对时间段序号  =  1
       起始时间，格式HH:MM  =  21:33
  起始日期，格式MM/DD/YYYY  =  2017-02-28
       结束时间，格式HH:MM  =  21:30
  结束日期，格式MM/DD/YYYY  =  2017-03-03
                配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询所有绝对时间段记录：
  ```
  LST ABSTIMERANGE:;
  ```
  ```

  RETCODE = 0  操作成功。

  绝对时间段信息
  --------------
  时间段名称    绝对时间段序号    起始时间，格式HH:MM    起始日期，格式MM/DD/YYYY    结束时间，格式HH:MM    结束日期，格式MM/DD/YYYY     配置域名称

  t1            1                 21:33                  2017-02-28                  21:30                  2017-03-03                   NULL
  t2            1                 06:54                  2017-03-05                  10:55                  2017-03-08                   NULL
  (结果个数 = 2)
  ---    END
  ```
- 查询一个时间段下的所有绝对时间段记录：
  ```
  LST ABSTIMERANGE: TIMERANGENAME="t1";
  ```
  ```

  RETCODE = 0  操作成功。

  绝对时间段信息
  --------------
                时间段名称  =  t1
            绝对时间段序号  =  1
       起始时间，格式HH:MM  =  21:33
  起始日期，格式MM/DD/YYYY  =  2017-02-28
       结束时间，格式HH:MM  =  21:30
  结束日期，格式MM/DD/YYYY  =  2017-03-03
                配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-ABSTIMERANGE.md`
