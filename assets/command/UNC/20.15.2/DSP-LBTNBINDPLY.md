---
id: UNC@20.15.2@MMLCommand@DSP LBTNBINDPLY
type: MMLCommand
name: DSP LBTNBINDPLY（查询业务服务ID与隧道组ID的关系）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LBTNBINDPLY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 隧道管理
- CSLB隧道绑定策略
status: active
---

# DSP LBTNBINDPLY（查询业务服务ID与隧道组ID的关系）

## 功能

该命令用于查询对端异地容灾实例的服务和隧道组关系，通过查询结果判断隧道组的绑定策略是否已经下发给CSLB，辅助定位隧道转发失败问题。

## 注意事项

该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRINSTID | 对端异地容灾实例ID | 可选必选说明：可选参数<br>参数含义：对端异地容灾实例ID。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无 |
| SRVID | 服务ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端异地容灾实例的服务ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LBTNBINDPLY]] · 业务服务ID与隧道组ID的关系（LBTNBINDPLY）

## 使用实例

查询指定对端异地容灾实例的服务和隧道组的关系。

DSP LBTNBINDPLY: GRINSTID=4;

```
%%DSP LBTNBINDPLY: GRINSTID=4;%%
RETCODE = 0  操作成功。

操作结果如下：
-------------------------
对端异地容灾实例ID 服务ID  隧道组ID 
4                  0       0 
4                  1       1 
(结果个数 = 2)
--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-LBTNBINDPLY.md`
