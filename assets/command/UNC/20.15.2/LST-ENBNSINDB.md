---
id: UNC@20.15.2@MMLCommand@LST ENBNSINDB
type: MMLCommand
name: LST ENBNSINDB（查询配置的eNodeB邻接关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ENBNSINDB
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- eNodeB邻接关系测试
status: active
---

# LST ENBNSINDB（查询配置的eNodeB邻接关系）

## 功能

**适用网元：MME**

此命令用于查询中手动添加的eNodeB邻接关系。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENBTYPE | eNodeB类型 | 可选必选说明：可选参数<br>参数含义：待查询邻接关系的中心eNodeB的类型。<br>取值范围：<br>- “HOME_ENODEB(Home_eNodeB)”：表示中心eNodeB类型为家庭基站，其标志长度为28位。<br>- “MACRO_ENODEB(Macro_eNodeB)”：表示中心eNodeB类型为宏基站，其标识长度为20位。<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：待查询邻接关系的中心eNodeB和邻接eNodeB共用的移动国家码。<br>取值范围：3位十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：待查询邻接关系的中心eNodeB和邻接eNodeB共用的移动网号。<br>取值范围：2～3位十进制数字<br>默认值：无 |
| ENBID | eNodeB标识 | 可选必选说明：可选参数<br>参数含义：待查询邻接关系的中心eNodeB的ID。<br>取值范围：0～268435455<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ENBNSINDB]] · 配置的eNodeB邻接关系（ENBNSINDB）

## 使用实例

查询所有手动添加的eNodeB邻接关系：

LST ENBNSINDB:;

```
%%LST ENBNSINDB:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
    eNodeB类型  =  Home_eNodeB
    移动国家码  =  123
      移动网号  =  01
    eNodeB标识  =  327697
邻接eNodeB个数  =  3
邻接eNodeB列表  =  327696&327698&327699
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询配置的eNodeB邻接关系(LST-ENBNSINDB)_72225939.md`
