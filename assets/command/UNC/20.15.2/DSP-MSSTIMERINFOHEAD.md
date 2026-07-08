---
id: UNC@20.15.2@MMLCommand@DSP MSSTIMERINFOHEAD
type: MMLCommand
name: DSP MSSTIMERINFOHEAD（查询定时器全局信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MSSTIMERINFOHEAD
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 定时器统计查询
status: active
---

# DSP MSSTIMERINFOHEAD（查询定时器全局信息）

## 功能

该命令用于查询定时器全局信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |

## 操作的配置对象

- [定时器全局信息（MSSTIMERINFOHEAD）](configobject/UNC/20.15.2/MSSTIMERINFOHEAD.md)

## 使用实例

查询定时器全局信息：

```
DSP MSSTIMERINFOHEAD:RUNAME = "VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
              定时器总数  =  8192
      当前使用定时器数量  =  6
              定时器峰值  =  6
          启动定时器次数  =  6
          停止定时器次数  =  0
同一时刻触发的定时器峰值  =  12
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询定时器全局信息（DSP-MSSTIMERINFOHEAD）_00440365.md`
