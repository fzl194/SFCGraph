---
id: UDG@20.15.2@MMLCommand@DSP UFPLATENCYSTAT
type: MMLCommand
name: DSP UFPLATENCYSTAT（显示UFP逐包转发时延度量开关）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: UFPLATENCYSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 时延统计
status: active
---

# DSP UFPLATENCYSTAT（显示UFP逐包转发时延度量开关）

## 功能

该命令用于显示UFP逐包转发时延度量开关。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLID | Cell ID | 可选必选说明：可选参数<br>参数含义：该参数表示PAE调试消息发送的CELLID，可以通过使用命令<br>[**DSP PAENODE**](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)<br>获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UFP逐包转发时延度量开关（UFPLATENCYSTAT）](configobject/UDG/20.15.2/UFPLATENCYSTAT.md)

## 使用实例

动态查询UFP逐包转发时延度量功能：

```
+++    UEG/*MEID:0 MENAME:UEG_1822*/        2024-03-20 10:55:47
O&M    #69
%%DSP UFPLATENCYSTAT:;%%
RETCODE = 0  操作成功

结果如下
------------------------
Cell ID					开关	虚拟局域网ID	剩余时长  

esa-pod-0__103__0			On	0|258|4095	225
csdb-pod-0__103__0			On	0|258|4095	225
ipapmexec-pod-b6988575-kmvm7__103__0	On	0|258|4095	225
isu-pod-1__103__0			On	0|258|4095	225
gcp-pod-1__103__0			On	0|258|4095	225			    
(结果如下 = 5)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示UFP逐包转发时延度量开关（DSP-UFPLATENCYSTAT）_88226712.md`
