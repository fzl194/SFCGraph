---
id: UNC@20.15.2@MMLCommand@LST ENBGPMEM
type: MMLCommand
name: LST ENBGPMEM（查询eNodeB群组成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ENBGPMEM
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- eNodeB管理
- eNodeB群组成员管理
status: active
---

# LST ENBGPMEM（查询eNodeB群组成员）

## 功能

**适用网元：MME**

该命令用于查询eNodeB群组成员记录。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENBGPID | eNodeB群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定eNodeB群组标识。<br>数据来源：本端规划<br>取值范围：1～2048<br>默认值：无 |
| ENBTYPE | eNodeB类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定eNodeB类型。<br>数据来源：整网规划<br>取值范围：<br>- “HOME_ENODEB(Home_eNodeB)”<br>- “MACRO_ENODEB(Macro_eNodeB)”<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动国家码<br>数据来源：整网规划<br>取值范围：3位的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：整网规划<br>取值范围：2～3位的十进制数字<br>默认值：无 |
| ENBID | eNodeB标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定eNodeB标识。<br>数据来源：整网规划<br>取值范围：0～268435455<br>默认值：无<br>说明：- 若参数“eNodeB类型”取值为“HOME_ENB(HOME_ENB)”，则该参数最大取值268435455。<br>- 若参数“eNodeB类型”取值为“MACRO_ENB(MACRO_ENB)”，则该参数最大取值1048575。<br>- 查询支持“ENBID”范围匹配，即如果用户输入范围内的某个值，则将该值对应的范围记录显示出来。 |

## 操作的配置对象

- [eNodeB群组成员（ENBGPMEM）](configobject/UNC/20.15.2/ENBGPMEM.md)

## 使用实例

查询所有eNodeB群组成员记录：

LST ENBGPMEM:;

```
%%LST ENBGPMEM:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
eNodeB群组标识  =  1
    eNodeB类型  =  Macro_eNodeB
    移动国家码  =  456
      移动网号  =  12
起始eNodeB标识  =  1234
终止eNodeB标识  =  1234
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询eNodeB群组成员(LST-ENBGPMEM)_72345207.md`
