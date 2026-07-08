---
id: UNC@20.15.2@MMLCommand@LST NGSCTPPARA
type: MMLCommand
name: LST NGSCTPPARA（查询N2接口SCTP协议参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGSCTPPARA
command_category: 查询类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCTP管理
status: active
---

# LST NGSCTPPARA（查询N2接口SCTP协议参数）

## 功能

适用NF：AMF

该命令用于查询N2接口SCTP协议参数。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGSCTPPARA]] · N2接口SCTP协议参数（NGSCTPPARA）

## 使用实例

查询N2接口SCTP协议参数的配置信息：

LST NGSCTPPARA:;

```
%%LST NGSCTPPARA:;%%
RETCODE = 0  操作成功

输出结果如下
------------
           SCTP数据绑定方式  =  不绑定
         绑定等待时长（ms）  =  30
               最大绑定包数  =  2
          防闪断定时器（s）  =  40
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGSCTPPARA.md`
