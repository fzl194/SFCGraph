---
id: UDG@20.15.2@MMLCommand@DSP MSSACLTBLINFO
type: MMLCommand
name: DSP MSSACLTBLINFO（查询软转发支撑访问控制列表详细信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSACLTBLINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- QACL统计查询
status: active
---

# DSP MSSACLTBLINFO（查询软转发支撑访问控制列表详细信息）

## 功能

该命令用于查询访问控制列表详细信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| TABLEID | 表ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示访问控制列表ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MSSACLTBLINFO]] · 软转发支撑访问控制列表详细信息（MSSACLTBLINFO）

## 使用实例

查询软转发支撑访问控制列表详细信息：

```
DSP MSSACLTBLINFO: TABLEID=0,RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
          访问控制列表初始化标识 = true
                    最大表项个数 = 2048
                  已使用表项个数 = 100
                        表项宽度 = 128
                线性表中表项个数 = 10
                      跳表的个数 = 1
                  跳表中表项个数 = 90
                    原子计数统计 = 0
访问控制列表内存使用量（K byte） = 300
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-MSSACLTBLINFO.md`
