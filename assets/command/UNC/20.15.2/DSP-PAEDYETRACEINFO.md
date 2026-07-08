---
id: UNC@20.15.2@MMLCommand@DSP PAEDYETRACEINFO
type: MMLCommand
name: DSP PAEDYETRACEINFO（显示PAE染色跟踪信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAEDYETRACEINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 染色流控
status: active
---

# DSP PAEDYETRACEINFO（显示PAE染色跟踪信息）

## 功能

该命令用于显示PAE染色跟踪信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLID | Cell ID | 可选必选说明：可选参数<br>参数含义：该参数表示PAE调试消息发送的CELL ID，可以通过使用命令DSP PAENODE获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PAEDYETRACEINFO]] · PAE染色跟踪信息（PAEDYETRACEINFO）

## 使用实例

动态查询PAE染色跟踪信息功能：

```
+++    UNC/*MEID:0 MENAME:env103*/        2024-12-13 00:57:57
O&M    #125
%%DSP PAEDYETRACEINFO:;%%
RETCODE = 0  操作成功

结果如下
------------------------
Cell ID                                染色全流控状态   CPU负载 (‰)      最大批收满比 (‰)           染色消耗CPU比 (‰)  

vup-pod-1__103__0                      false            3                 0                           0                        
gtp-pod-67d6976f98-wlmxx__103__0       false            1                 0                           0                        
sbim-pod-7b997d9594-vcq96__103__0      false            2                 0                           0                        
vam-pod-7dbc778c6-bbvpt__103__0        false            1                 0                           0                        
appctrl-pod-868577bbd-dc7mf__103__0    false            2                 0                           0                        
sbim-pod-7b997d9594-77jg5__103__0      false            2                 0                           0                        
(结果如下 = 6)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PAEDYETRACEINFO.md`
