---
id: UNC@20.15.2@MMLCommand@LST QBCGLBPARA
type: MMLCommand
name: LST QBCGLBPARA（查询QBC计费全局参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QBCGLBPARA
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 全局配置
status: active
---

# LST QBCGLBPARA（查询QBC计费全局参数）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询QBC计费全局参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@QBCGLBPARA]] · QBC计费全局参数（QBCGLBPARA）

## 使用实例

查询QBC计费全局参数：

```
%%LST QBCGLBPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
 激活阶段QoSFlow上报模式  =  不上报
QoSFlow级Trigger填写方式  =  不使能
     QoSFlow时长计算方式  =  PACKETTRIGGERED
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-QBCGLBPARA.md`
