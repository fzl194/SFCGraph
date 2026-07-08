---
id: UNC@20.15.2@MMLCommand@LST NRFVISITPLY
type: MMLCommand
name: LST NRFVISITPLY（查询NRF拜访地默认策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFVISITPLY
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF国际漫游参数管理
status: active
---

# LST NRFVISITPLY（查询NRF拜访地默认策略）

## 功能

**适用NF：NRF**

此命令用于查询NRF作为拜访地NRF时跨PLMN请求的默认策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [NRF拜访地默认策略（NRFVISITPLY）](configobject/UNC/20.15.2/NRFVISITPLY.md)

## 使用实例

查询漫入默认策略。

```
%%LST NRFVISITPLY:;%%
RETCODE = 0  操作成功

结果如下
--------
        是否支持跨PLMN订阅  =  打开
  订阅是否进行Location改造  =  打开
      订阅转发是否删除PLMN  =  打开
跨PLMN转发是否剥离目的PLMN  =  打开
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NRF拜访地默认策略（LST-NRFVISITPLY）_24956638.md`
