---
id: UNC@20.15.2@MMLCommand@DSP ENBATTR
type: MMLCommand
name: DSP ENBATTR（显示eNodeB属性）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ENBATTR
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
- eNodeB属性信息管理
status: active
---

# DSP ENBATTR（显示eNodeB属性）

## 功能

**适用网元：MME**

该命令用于查询指定eNodeB的属性信息。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENBTYPE | eNodeB类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定eNodeB的类型。<br>取值范围：<br>- “HOME_ENODEB(Home eNodeB)”：表示eNodeB类型为家庭基站，其标志长度为28位。<br>- “MACRO_ENODEB(Macro eNodeB)”：表示eNodeB类型为宏基站，其标识长度为20位。<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定eNodeB的移动国家码。<br>取值范围：3位十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定eNodeB的移动网号。<br>取值范围：2～3位十进制数字<br>默认值：无 |
| ENBID | eNodeB标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定eNodeB的标识。<br>取值范围：0～268435455<br>默认值：无<br>说明：- 若参数“eNodeB类型”取值为“HOME_ENODEB(Home eNodeB)”，则该参数最大取值268435455。<br>- 若参数“eNodeB类型”取值为“MACRO_ENODEB(Macro eNodeB)”，则该参数最大取值1048575。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ENBATTR]] · eNodeB属性（ENBATTR）

## 使用实例

查询一个eNodeB的UE无线寻呼能力指示信息，eNodeB的 “eNodeB类型” 为 “MACRO_ENODEB(Macro eNodeB)” ， “移动国家码” 为 “123” ， “移动网号” 为 “01” ， “eNodeB标识” 为 “327697” ：

DSP ENBATTR: ENBTYPE=MACRO_ENODEB, MCC="123", MNC="01", ENBID=327697;

```
%%DSP ENBATTR: ENBTYPE=MACRO_ENODEB, MCC="123", MNC="01", ENBID=327697;%%
RETCODE = 0  操作成功。

 输出结果如下
--------------
                eNodeB类型  =  Macro eNodeB
                移动国家码  =  123
                  移动网号  =  01
                eNodeB标识  =  327697
        UE无线寻呼能力指示  =  不支持
eNodeB覆盖增强寻呼能力指示  =  不支持
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示eNodeB属性(DSP-ENBATTR)_72345861.md`
