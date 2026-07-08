---
id: UNC@20.15.2@MMLCommand@DSP GNBENBNEIBS
type: MMLCommand
name: DSP GNBENBNEIBS（显示en-gNB邻接的eNodeB）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GNBENBNEIBS
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- en-gNB邻接的eNodeB
status: active
---

# DSP GNBENBNEIBS（显示en-gNB邻接的eNodeB）

## 功能

**适用NF：MME**

查询指定en-gNB邻接的eNodeB。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug;system-ug;monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家代码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定en-gNB的移动国家码。<br>取值范围：3位数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定en-gNB的移动网号。<br>取值范围：2～3位数字<br>默认值：无 |
| ENGNBID | en-gNB标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定en-gNB的标识。<br>取值范围：0～4294967295 (数值型)<br>默认值：无 |
| ENGNBBITLEN | en-gNB ID有效比特长度 | 可选必选说明：必选参数。<br>参数含义：该参数用于显示en-gNB ID有效比特长度。<br>取值范围：整数类型，取值范围是22~32。<br>默认值：无 |

## 操作的配置对象

- [en-gNB邻接的eNodeB（GNBENBNEIBS）](configobject/UNC/20.15.2/GNBENBNEIBS.md)

## 使用实例

查询移动国家码为263，移动网号为127，标识为14764，有效比特长度为24的en-gNB的邻接eNodeB列表：

DSP GNBENBNEIBS: MCC="263", MNC="127", ENGNBID=14764, ENGNBBITLEN=24;

```
%%DSP GNBENBNEIBS: MCC="263", MNC="127", ENGNBID=14764, ENGNBBITLEN=24;%%
RETCODE = 0  操作成功

查询结果如下
------------------------
eNodeB类型    移动国家代码    移动网号  eNodeB标识   跟踪区域码   PLMNS  

Macro_eNodeB  123             03        143377       8961        12303  
Macro_eNodeB  123             03        143409       8961        12303  
Macro_eNodeB  123             03        143378       8961        12303  
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示en-gNB邻接的eNodeB（DSP-GNBENBNEIBS）_39386845.md`
