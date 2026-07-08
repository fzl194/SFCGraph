---
id: UNC@20.15.2@MMLCommand@LST NRFBIGPKGPARA
type: MMLCommand
name: LST NRFBIGPKGPARA（查询NRF大包控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFBIGPKGPARA
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF大包控制参数
status: active
---

# LST NRFBIGPKGPARA（查询NRF大包控制参数）

## 功能

**适用NF：NRF**

该命令用于查询NRF大包控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFBIGPKGPARA]] · NRF大包控制参数（NRFBIGPKGPARA）

## 使用实例

查询NRF大包控制参数：

```
%%LST NRFBIGPKGPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
        单NF的最大号段数量  =  20000
  服务发现返回的最大号段数  =  40000
       最大报文长度(KByte)  =  200
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFBIGPKGPARA.md`
