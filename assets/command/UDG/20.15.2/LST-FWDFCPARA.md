---
id: UDG@20.15.2@MMLCommand@LST FWDFCPARA
type: MMLCommand
name: LST FWDFCPARA（查询转发面流控参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FWDFCPARA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 操作维护
- 系统调测
- 转发面流控参数
status: active
---

# LST FWDFCPARA（查询转发面流控参数）

## 功能

该命令用于查询CSLB转发面流控参数。

## 注意事项

- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组；

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/FWDFCPARA]] · 转发面流控参数（FWDFCPARA）

## 使用实例

查询所有已配置的CSLB转发面流控参数。

```
%%LST FWDFCPARA:;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
流控类型    一级流控阈值(pps)  二级流控阈值(pps)  

ICMP        1024               60                 
IPS_DETECT  3200               800                
TCP_SYN     200                10                
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-FWDFCPARA.md`
