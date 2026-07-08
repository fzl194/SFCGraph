---
id: UDG@20.15.2@MMLCommand@DSP MSSSCHWORKGROUP
type: MMLCommand
name: DSP MSSSCHWORKGROUP（显示调度组工作类型信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSSCHWORKGROUP
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- MSS 调测命令
status: active
---

# DSP MSSSCHWORKGROUP（显示调度组工作类型信息）

## 功能

该命令用于显示调度组工作类型信息。

## 注意事项

- 该命令执行后立即生效。
- 使用此命令前需要使用**[SET MSSDEBUGSWITCHM](设置维测信息统计开关（SET MSSDEBUGSWITCHM）_93243682.md)**打开MSS维测统计信息开关。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务实例号。 |
| GROUPID | 调度组ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示调度组ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：使用<br>**[DSP MSSSCHSUMTAILM](显示调度部署详细信息（DSP MSSSCHSUMTAILM）_92520023.md)**<br>查看当前调度的调度组号。 |
| QOSID | 优先级队列ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示优先级队列ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MSSSCHWORKGROUP]] · 调度组工作类型信息（MSSSCHWORKGROUP）

## 使用实例

显示微服务类型为aa的微服务实例bb内调度组2，优先级队列ID为0的信息：

```
DSP MSSSCHWORKGROUP: CELLTYPE="aa", CELLINSTANCE="bb", GROUPID=2, QOSID=0;%
```

```
RETCODE = 0  操作成功

结果如下:
---------
                         任务类型  =  515
                     任务调度次数  =  11
任务调度间隔最大值（microsecond）  =  990591
任务调度间隔平均值（microsecond）  =  401227
任务处理时间最大值（microsecond）  =  4
任务处理时间平均值（microsecond）  =  2
                 任务回调注册次数  =  1
                     添加任务计数  =  11
                     获取任务计数  =  11
                 添加任务失败计数  =  0
         任务处理占用CPU比率（%）  =  100
                   任务回调函数名  =  ufpTimerWorkCallback
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-MSSSCHWORKGROUP.md`
