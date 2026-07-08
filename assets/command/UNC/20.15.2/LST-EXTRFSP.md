---
id: UNC@20.15.2@MMLCommand@LST EXTRFSP
type: MMLCommand
name: LST EXTRFSP（查询扩展RFSP策略组成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: EXTRFSP
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- RFSP管理
- 扩展RFSP策略管理
status: active
---

# LST EXTRFSP（查询扩展RFSP策略组成员）

## 功能

**适用网元：SGSN、MME**

该命令用于查看扩展RFSP策略组中的策略。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | 类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该扩展RFSP策略的类型。<br>数据来源：整网规划<br>取值范围：<br>- “SPEC_MOVE_SUB(指定的移动用户)”<br>默认值：无 |
| ARETYPE | 区域类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定扩展RFSP策略控制区域范围类型。<br>前提条件：该参数在“TYPE（类型）”参数配置为“SPEC_MOVE_SUB(指定的移动用户)”后生效。<br>数据来源：整网规划<br>取值范围：<br>- “TAGP(跟踪区群组)”<br>- “ENBGP(eNodeB群组)”<br>默认值：无 |
| TAGPID | 跟踪区群组标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定跟踪区群组标识。<br>前提条件：该参数在<br>“ARETYPE（区域类型）”<br>参数配置为<br>“TAGP(跟踪区群组)”<br>后生效。<br>数据来源：整网规划<br>取值范围：1~2048<br>默认值：无 |
| ENBGPID | eNodeB群组标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定eNodeB群组标识。<br>前提条件：该参数在<br>“ARETYPE（区域类型）”<br>参数配置为<br>“ENBGP(eNodeB群组)”<br>后生效。<br>数据来源：整网规划<br>取值范围：1~2048<br>默认值：无 |

## 操作的配置对象

- [扩展RFSP策略组成员（EXTRFSP）](configobject/UNC/20.15.2/EXTRFSP.md)

## 使用实例

查询扩展RFSP策略组中的策略：

LST EXTRFSP:;

```
%%LST EXTRFSP:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
                      类型  =  指定的移动用户
                  区域类型  =  跟踪区群组
            跟踪区群组标识  =  1
            eNodeB群组标识  =  NULL
                  目标RFSP  =  111
          目标RFSP重发次数  =  2
          目标RFSP发送抑制  =  否
                  抑制周期  =  0
抑制周期内目标RFSP重发次数  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询扩展RFSP策略组成员(LST-EXTRFSP)_72345135.md`
