---
id: UNC@20.15.2@MMLCommand@LST HOMEGROUP
type: MMLCommand
name: LST HOMEGROUP（查询Home Group）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HOMEGROUP
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- GGSN和P-GW Proxy
- Home Group
status: active
---

# LST HOMEGROUP（查询Home Group）

## 功能

**适用NF：PGW-C、GGSN**

该命令用于查询Home Group配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOMEGROUPINDX | Home Group编号 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Home Group的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HOMEGROUP]] · Home Group（HOMEGROUP）

## 使用实例

查询“Home Group编号”为“1”的Home Group配置：

```
%%LST HOMEGROUP: HOMEGROUPINDX=1;%%
RETCODE = 0  操作成功

结果如下
------------------------
                Home Group编号  =  1
              Home Group优先级  =  65535
Home Group绑定的用户号码段组名  =  grp1
                计费特征组名称  =  c1
2B2C漫游双DNN特性功能开关 = DISABLE
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Home-Group（LST-HOMEGROUP）_88613381.md`
