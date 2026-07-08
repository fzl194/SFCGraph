---
id: UNC@20.15.2@MMLCommand@LST CHRRPTLOCINFO
type: MMLCommand
name: LST CHRRPTLOCINFO（查询CHR本地存盘位置配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHRRPTLOCINFO
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- CHR管理
- CHR本地存盘位置
status: active
---

# LST CHRRPTLOCINFO（查询CHR本地存盘位置配置）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于显示需要进行CHR本地存盘的用户的位置过滤条件，包括N2TAC、S1TAC、LACRAC、eNodeB、gNodeB。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCTYPE | 位置类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定位置类型。<br>数据来源：本端规划<br>取值范围：<br>- N2TAC（N2跟踪区域码）<br>- S1TAC（S1跟踪区域码）<br>- LACRAC（位置区编码和路由区编码）<br>- ENODEBIP（eNodeB IP地址）<br>- GNODEBIP（gNodeB IP地址）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CHRRPTLOCINFO]] · CHR本地存盘位置配置（CHRRPTLOCINFO）

## 使用实例

显示N2TAC类型的CHR本地存盘配置：

```
%%LST CHRRPTLOCINFO: LOCTYPE=N2TAC;%%
RETCODE = 0  操作成功

结果如下
------------------------
    位置类型  =  N2TAC
       N2TAC  =  0x123123
流程模板索引  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CHRRPTLOCINFO.md`
