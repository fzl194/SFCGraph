---
id: UNC@20.15.2@MMLCommand@LST SBIDIALTEST
type: MMLCommand
name: LST SBIDIALTEST（查询间接路由拨测用户配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SBIDIALTEST
command_category: 查询类
applicable_nf:
- SMF
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 拨测管理
status: active
---

# LST SBIDIALTEST（查询间接路由拨测用户配置）

## 功能

**适用NF：SMF、AMF**

该命令通过起始SUPI/GPSI查询一组拨测用户。

## 注意事项

- 相同拨测用户范围的两条记录的拨测用户范围不可以重叠。
- 该命令的匹配拨测用户的方式为全匹配。
- 该命令每条记录配置的拨测用户数不大于100。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERRANGE | 用户标识类型 | 可选必选说明：可选参数<br>参数含义：该参数用于配置拨测用户范围。<br>数据来源：本端规划<br>取值范围：<br>- SUPI（SUPI）<br>- GPSI（GPSI）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SBIDIALTEST]] · 间接路由拨测用户配置（SBIDIALTEST）

## 使用实例

查询一条拨测用户配置，UserRange类型为SUPI，待拨测用着SUPI长度为15位，用户范围为123450000000000~123460000000000。

```
%%LST SBIDIALTEST:;%%
RETCODE = 0  操作成功

结果如下
------------------------
  ENDSUPI  =  123460000000000
  ENDGPSI  =  NULL
USERRANGE  =  SUPI
BEGINSUPI  =  123450000000000
BEGINGPSI  =  NULL
(结果个数 = 1)

----    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SBIDIALTEST.md`
