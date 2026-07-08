---
id: UNC@20.15.2@MMLCommand@LST NRFRGNPREFPLY
type: MMLCommand
name: LST NRFRGNPREFPLY（查询NRF区域优选策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFRGNPREFPLY
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF区域优选管理
status: active
---

# LST NRFRGNPREFPLY（查询NRF区域优选策略）

## 功能

**适用NF：NRF**

该命令用于查询NRF区域优选策略。该命令功能暂不生效。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFRGNPREFPLY]] · NRF区域优选策略（NRFRGNPREFPLY）

## 使用实例

查询NRF区域优选策略：

```
LST NRFRGNPREFPLY:;
%%LST NRFRGNPREFPLY:;%%
RETCODE = 0  操作成功

结果如下
--------
          DNNI区域优选功能开关 = 打开
          DNAI区域优选功能开关 = 打开
     实例标识中区域信息起始位  =  26
       实例标识中区域信息长度  =  2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFRGNPREFPLY.md`
