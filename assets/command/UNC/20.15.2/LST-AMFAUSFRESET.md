---
id: UNC@20.15.2@MMLCommand@LST AMFAUSFRESET
type: MMLCommand
name: LST AMFAUSFRESET（查询AMF的AUSF故障处理策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFAUSFRESET
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 可靠性管理
- AMF的AUSF故障处理策略
status: active
---

# LST AMFAUSFRESET（查询AMF的AUSF故障处理策略）

## 功能

**适用NF：AMF**

该命令用于查询AMF的AUSF故障处理策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AMFAUSFRESET]] · AMF的AUSF故障处理策略（AMFAUSFRESET）

## 使用实例

查询AMF的AUSF故障处理策略，执行如下命令：

```
%%LST AMFAUSFRESET:;%%
RETCODE = 0  操作成功

结果如下
--------
recoveryTime变化时重选AUSF开关  =  打开
                      扫描模式  =  默认扫描模式
               扫描速率(个/秒)  =  2
              单位扫描时间(秒)  =  3
                  单位扫描个数  =  2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AMFAUSFRESET.md`
