---
id: UNC@20.15.2@MMLCommand@LST AMFFCPARA
type: MMLCommand
name: LST AMFFCPARA（查询AMF自保流控参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFFCPARA
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 拥塞控制
- AMF流控参数
status: active
---

# LST AMFFCPARA（查询AMF自保流控参数）

## 功能

**适用NF：AMF**

该命令用于查询AMF自保流控参数。

## 注意事项

“CPU过载控制门限”参数在UNC 20.5.1版本及之后不再使用。“阈值”后续通过LST FCPARAM命令查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFFCPARA]] · AMF自保流控参数（AMFFCPARA）

## 使用实例

查询AMF自保流控参数：

```
%%LST AMFFCPARA:;%%
RETCODE = 0  操作成功

输出结果如下
------------------------
              CPU过载控制门限(%)  =  70
                        流控措施  =  丢弃
           Backoff timer信元开关  =  关闭
         Backoff timer最小值(秒)  =  900
         Backoff timer最大值(秒)  =  1800
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AMFFCPARA.md`
