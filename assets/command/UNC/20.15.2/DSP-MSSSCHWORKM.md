---
id: UNC@20.15.2@MMLCommand@DSP MSSSCHWORKM
type: MMLCommand
name: DSP MSSSCHWORKM（显示调度工作类型信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MSSSCHWORKM
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- MSS 调测命令
status: active
---

# DSP MSSSCHWORKM（显示调度工作类型信息）

## 功能

该命令用于显示调度工作类型信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务实例号。 |
| THREADID | 线程ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示线程ID。如果不输入该参数，显示所有线程的调度工作类型。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无<br>配置原则：使用<br>**[DSP MSSSCHSUMTAILM](显示调度部署详细信息（DSP MSSSCHSUMTAILM）_92520023.md)**<br>查看线程逻辑ID。 |

## 操作的配置对象

- [调度工作类型信息（MSSSCHWORKM）](configobject/UNC/20.15.2/MSSSCHWORKM.md)

## 使用实例

显示类型为aa的微服务bb内调度工作类型线程信息：

```
DSP MSSSCHWORKM: CELLTYPE="aa",CELLINSTANCE="bb",THREADID=1;
```

```
RETCODE = 0  操作成功。

结果如下
--------
任务类型    任务调度次数    任务调度间隔最大值（microsecond）    任务调度间隔平均值（microsecond）    任务处理时间最大值（microsecond）    任务处理时间平均值（microsecond）    任务回调注册次数    添加任务计数   获取任务计数   添加任务失败计数    任务处理占用CPU比率（%）    任务回调函数名       
							
50          73673           3607                                 9                                    106                                  3                                    1                   --             0              --                  98                          PAE_DP_RunSch        
514         32              3610                                 9                                    3542                                 1                                    1                   --             0              --                  0                           ufpTimerWorkCallback 

(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示调度工作类型信息（DSP-MSSSCHWORKM）_92520013.md`
