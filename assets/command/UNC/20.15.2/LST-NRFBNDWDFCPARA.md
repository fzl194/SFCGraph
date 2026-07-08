---
id: UNC@20.15.2@MMLCommand@LST NRFBNDWDFCPARA
type: MMLCommand
name: LST NRFBNDWDFCPARA（查询NRF带宽流控配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFBNDWDFCPARA
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF流控参数
status: active
---

# LST NRFBNDWDFCPARA（查询NRF带宽流控配置）

## 功能

**适用NF：NRF**

该命令用于查询NRF带宽流控配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [NRF带宽流控配置（NRFBNDWDFCPARA）](configobject/UNC/20.15.2/NRFBNDWDFCPARA.md)

## 使用实例

查询NRF带宽流控配置：

```
LST NRFBNDWDFCPARA:;
%%LST NRFBNDWDFCPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
		  内部服务发现带宽流控功能开关  =  打开
			  内部服务发现带宽流控阈值  =  10
分层转发内部服务发现的带宽流控功能开关  =  关闭
	分层转发内部服务发现的带宽流控阈值  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NRF带宽流控配置（LST-NRFBNDWDFCPARA）_19010713.md`
