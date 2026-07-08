---
id: UDG@20.15.2@MMLCommand@DSP AFUSRDETECTST
type: MMLCommand
name: DSP AFUSRDETECTST（显示欺诈用户检测结果）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: AFUSRDETECTST
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务防欺诈
- 显示欺诈用户检测结果
status: active
---

# DSP AFUSRDETECTST（显示欺诈用户检测结果）

## 功能

**适用NF：UPF**

该命令用来显示可疑欺诈用户信息，历史记录，防欺诈库匹配次数等。

## 注意事项

使用该命令查询前，需要通过SET AFUSRDETECT命令配置计费欺诈用户检测功能开关。使用命令DSP AFUSRDETECT查看开关状态为DISABLE，不显示统计信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESOURCEUNIT | Pod名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/AFUSRDETECTST]] · 欺诈用户检测结果（AFUSRDETECTST）

## 使用实例

查询用户防欺诈流量检测统计信息：

```
DSP AFUSRDETECTST:;
```

```

RETCODE = 0  操作成功。

计费欺诈用户检测查询结果
------------------------
Pod名称          查询结果                                                                                                                                                                                                                                                                                                                                                                                                                                                     

ssgpod-0136-30-0-251    1-From (09:09 2020/05/21) to (09:09 2020/05/21):
--------------------------------------------------------------------------------------------------
No.     MSISDN        SpecialRG(KB)    Total(KB)      Ratio(%)     Af-DB-Stats     DetectTime
--------------------------------------------------------------------------------------------------
  1   8613801040011              6             6         100              0      11:27 2017/10/27
--------------------------------------------------------------------------------------------------

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-AFUSRDETECTST.md`
