---
id: UNC@20.15.2@MMLCommand@LST SDCFG
type: MMLCommand
name: LST SDCFG（查询签约数据配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SDCFG
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
- 业务安全管理
- 签约数据管理
- 签约数据信息
status: active
---

# LST SDCFG（查询签约数据配置）

## 功能

**适用网元：SGSN、MME**

该命令用于查询签约数据配置。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SDCFG]] · 签约数据配置（SDCFG）

## 使用实例

查询签约数据配置中所有相关的功能项:

LST SDCFG:;

```
%%LST SDCFG:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
                     禁止所有呼出  =  不支持
                 禁止所有国际呼出  =  不支持
           禁止所有非归属国家呼出  =  不支持
               禁止所有区域间呼出  =  不支持
           禁止非归属国家区间呼出  =  不支持
         禁止非归属国区间国际呼出  =  不支持
           禁止用户所有分组域业务  =  不支持
禁止漫游用户通过HPLMN的接入点接入  =  不支持
禁止漫游用户通过VPLMN的接入点接入  =  不支持
         运营商自定义ODB类型1功能  =  不支持
         运营商自定义ODB类型2功能  =  不支持
         运营商自定义ODB类型3功能  =  不支持
         运营商自定义ODB类型4功能  =  不支持
                Super-Charger功能  =  不支持
（结果个数 = 1）

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SDCFG.md`
