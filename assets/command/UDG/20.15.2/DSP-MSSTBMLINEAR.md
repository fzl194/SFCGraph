---
id: UDG@20.15.2@MMLCommand@DSP MSSTBMLINEAR
type: MMLCommand
name: DSP MSSTBMLINEAR（通过关键字查询线性表的结果）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSTBMLINEAR
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 表项管理统计查询
status: active
---

# DSP MSSTBMLINEAR（通过关键字查询线性表的结果）

## 功能

该命令用于关键字查询线性表的结果。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| TABLEID | 表号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示表号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| LINEARINDEX | 线性索引 | 可选必选说明：必选参数<br>参数含义：该参数用于表示线性索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| MATCHTYPE | 匹配类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示匹配类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- exact：精确匹配。<br>- noexact：模糊匹配。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MSSTBMLINEAR]] · 通过关键字查询线性表的结果（MSSTBMLINEAR）

## 使用实例

查询使用关键字查询线性表的结果：

```
DSP MSSTBMLINEAR:TABLEID = 1,LINEARINDEX = 1,MATCHTYPE = exact,RUNAME = "VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
--------
    初始化标识  =  TRUE
  表项存在标识  =  TRUE
哈希桶表项数量  =  0
        表类型  =  POOL_LINEAR1
转发表前缀长度  =  0
      表项索引  =  0
        错误码  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-MSSTBMLINEAR.md`
