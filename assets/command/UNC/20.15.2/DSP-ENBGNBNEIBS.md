---
id: UNC@20.15.2@MMLCommand@DSP ENBGNBNEIBS
type: MMLCommand
name: DSP ENBGNBNEIBS（显示eNodeB邻接的en-gNB）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ENBGNBNEIBS
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
- eNodeB邻接的en-gNB
status: active
---

# DSP ENBGNBNEIBS（显示eNodeB邻接的en-gNB）

## 功能

**适用NF：MME**

查询指定eNodeB邻接的en-gNB。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug;system-ug;monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询类型。<br>取值范围：<br>- “BRIEF（简要信息）”<br>- “DETAIL（详细信息）”<br>默认值：无 |
| ENBTYPE | eNodeB类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定eNodeB的类型。<br>取值范围：<br>- “HOME_ENODEB(Home_eNodeB)”<br>- “MACRO_ENODEB(Macro_eNodeB)”<br>默认值：无 |
| MCC | 移动国家代码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定eNodeB的移动国家码。<br>取值范围：3位数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定eNodeB的移动网号。<br>取值范围：2～3位数字<br>默认值：无 |
| ENBID | eNodeB标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定eNodeB的标识。<br>取值范围：0～268435455(数值型)<br>默认值：无 |

## 操作的配置对象

- [eNodeB邻接的en-gNB（ENBGNBNEIBS）](configobject/UNC/20.15.2/ENBGNBNEIBS.md)

## 使用实例

查询移动国家码为263，移动网号为127，标识为210652的eNodeB的邻接en-gnb列表：

DSP ENBGNBNEIBS: QUERYTYPE=BRIEF, ENBTYPE=MACRO_ENODEB, MCC="263", MNC="127", ENBID=210652;

```
%%DSP ENBGNBNEIBS: QUERYTYPE=BRIEF, ENBTYPE=MACRO_ENODEB, MCC="263", MNC="127", ENBID=210652;%%
RETCODE = 0  操作成功

操作结果如下
------------
移动国家代码  移动网号  en-gNB标识  en-gNB ID有效比特长度  

263           127       42609        24                      
263           127       42610        24                      
263           127       42611        24                      
263           127       42612        24                      
263           127       42613        24                      
263           127       42614        24                      
263           127       42615        24                      
263           127       42616        24                                           
(结果个数 = 8)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示eNodeB邻接的en-gNB（DSP-ENBGNBNEIBS）_88506886.md`
