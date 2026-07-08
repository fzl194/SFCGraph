---
id: UNC@20.15.2@MMLCommand@DSP ENBNEIBS
type: MMLCommand
name: DSP ENBNEIBS（显示eNodeB邻接关系）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ENBNEIBS
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
- eNodeB邻接关系管理
status: active
---

# DSP ENBNEIBS（显示eNodeB邻接关系）

## 功能

**适用网元：MME**

查询指定中心eNodeB的邻接eNodeB列表，对系统无影响。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENBTYPE | eNodeB类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定中心eNodeB的类型。<br>取值范围：<br>- “HOME_ENODEB(Home_eNodeB)”<br>- “MACRO_ENODEB(Macro_eNodeB)”<br>默认值：无 |
| MCC | 移动国家代码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定中心eNodeB的移动国家码。<br>取值范围：3位数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定中心eNodeB的移动网号。<br>取值范围：2～3位数字<br>默认值：无 |
| ENBID | eNodeB 标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定中心eNodeB的标识。<br>取值范围：0～268435455(数值型)<br>默认值：无 |

## 操作的配置对象

- [eNodeB邻接关系（ENBNEIBS）](configobject/UNC/20.15.2/ENBNEIBS.md)

## 使用实例

查询移动国家码为123，移动网号为03，标识为326的中心eNodeB的邻接eNodeB列表：

DSP ENBNEIBS: ENBTYPE=HOME_ENODEB, MCC="123", MNC="03", ENBID=326;

```
O&M  #61
%%DSP ENBNEIBS: ENBTYPE=HOME_ENODEB, MCC="123", MNC="03", ENBID=326;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
     eNodeB类型    移动国家码    移动网号     eNodeB标识
     Home_eNodeB   123           03           327
     Home_eNodeB   123           03           328
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示eNodeB邻接关系(DSP-ENBNEIBS)_26146258.md`
