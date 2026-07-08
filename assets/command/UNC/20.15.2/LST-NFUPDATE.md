---
id: UNC@20.15.2@MMLCommand@LST NFUPDATE
type: MMLCommand
name: LST NFUPDATE（查询NF更新方式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFUPDATE
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- NF更新管理
status: active
---

# LST NFUPDATE（查询NF更新方式）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG**

该命令用于查询NF信息更新到NRF时的方式。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFUPDATE]] · 更新NF注册信息（NFUPDATE）

## 使用实例

查询当前NF信息更新到NRF时采用的方式。

```
%%LST NFUPDATE:;%%
RETCODE = 0  操作成功

结果如下
--------
      Patch更新缓存最大数量  =  5
Patch更新缓存定时器时长(分钟)  =  2
( 结果个数= 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NFUPDATE.md`
