---
id: UNC@20.15.2@MMLCommand@DSP AMFMBSSESNUM
type: MMLCommand
name: DSP AMFMBSSESNUM（显示AMF组播广播会话数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: AMFMBSSESNUM
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G组播广播管理
- AMF组播广播管理
- 显示AMF组播广播会话数
status: active
---

# DSP AMFMBSSESNUM（显示AMF组播广播会话数）

## 功能

**适用NF：AMF**

该命令用于查询AMF组播广播会话数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SESSIONTYPE | 会话类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询的会话类型。<br>数据来源：本端规划<br>取值范围：<br>- BROADCAST（广播）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AMFMBSSESNUM]] · AMF组播广播会话数（AMFMBSSESNUM）

## 使用实例

查看AMF上的广播会话数，执行如下命令：

```
%%DSP AMFMBSSESNUM: SESSIONTYPE=BROADCAST;%%
RETCODE = 0  操作成功

结果如下
------------------------
POD ID     MBS会话数  

gtp-pod-0  2                       
total      2                 
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-AMFMBSSESNUM.md`
