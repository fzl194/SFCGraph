---
id: UNC@20.15.2@MMLCommand@DSP RESTORELAT
type: MMLCommand
name: DSP RESTORELAT（显示容灾关系信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RESTORELAT
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- MME链式备份管理
- MME容灾管理
- 容灾功能调测
status: active
---

# DSP RESTORELAT（显示容灾关系信息）

## 功能

**适用网元：MME**

本命令用于查询系统使用的备份关系信息。输出结果有两种报表。报表1显示设备级的备份关系，报表2显示设备的Sdup接口业务IP信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESULTTP | 结果类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指示查询的结果类型。<br>数据来源：本端规划<br>取值范围：<br>- “NORMAL（正常信息）”：输出结果为正在使用的备份关系结果。<br>- “ABNORMAL（异常信息）”：输出结果为错误的备份关系配置结果。<br>默认值：<br>“NORMAL（正常信息）”<br>说明：“ABNORMAL（异常信息）”<br>按照异常的类型，分为多个报表输出。比如：<br>- 1个MME没有对应的备份MME。<br>- 1个MME存在2个以上（含2个）的备份MME。<br>- 1个MME为2个以上（含2个）MME提供容灾<br>- 1个MME在多个备份环中出现。<br>- 备份关系的域名数量超出规格。<br>- 备份关系的IP数量超出规格。<br>- Sdup接口IP地址与备份关系的IP地址配置不匹配。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESTORELAT]] · 容灾关系信息（RESTORELAT）

## 使用实例

显示容灾关系信息：

DSP RESTORELAT:;

```
%%DSP RESTORELAT:;%%
RETCODE = 0  操作成功

输出结果如下：
-------------------------
       备份环编号  =  1
备份环内的设备标识  =  23 26 
(结果个数 = 1)

仍有后续报告输出
---    END

+++    mcr        2017-02-15 13:55:47
O&M   #HWHandle=173
%%DSP RESTORELAT:;%%
RETCODE = 0  操作成功

输出结果如下：
-------------------------
 备份环编号         设备标识      源设备标识 备份设备标识  IPv4地址    IPv6地址  IP地址所属主机名优先级  IP地址所属主机名权重  IP地址优先级  IP地址权重

 1                   23            26         26           10.2.3.30    ::        0                       100                   127           127              
 1                   26            23         23           10.2.6.30    ::        0                       100                   127           127              
(结果个数 = 2)

共有2个报表
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-RESTORELAT.md`
