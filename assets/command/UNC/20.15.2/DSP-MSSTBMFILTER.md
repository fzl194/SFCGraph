---
id: UNC@20.15.2@MMLCommand@DSP MSSTBMFILTER
type: MMLCommand
name: DSP MSSTBMFILTER（查询MSS表项开关过滤状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MSSTBMFILTER
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

# DSP MSSTBMFILTER（查询MSS表项开关过滤状态）

## 功能

该命令用于查询表项开关过滤状态。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示的RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSSTBMFILTER]] · MSS表项开关过滤状态（MSSTBMFILTER）

## 使用实例

查询表项开关过滤状态：

```
DSP MSSTBMFILTER:RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
            开关使能  =  TRUE
                表ID  =  all
              表类型  =  linear
          线性索引值  =  1
          哈希关键字  =  NULL
        虚拟专用网号  =  NULL
            IPv4地址  =  NULL
            IPv6地址  =  NULL
            掩码长度  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询MSS表项开关过滤状态（DSP-MSSTBMFILTER）_49802174.md`
