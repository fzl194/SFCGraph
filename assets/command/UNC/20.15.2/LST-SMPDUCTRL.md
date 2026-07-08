---
id: UNC@20.15.2@MMLCommand@LST SMPDUCTRL
type: MMLCommand
name: LST SMPDUCTRL（查询PDU会话控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMPDUCTRL
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NAS传输管理
- PDU会话控制管理
status: active
---

# LST SMPDUCTRL（查询PDU会话控制参数）

## 功能

**适用NF：AMF**

该命令用于查询AMF管理PDU会话的控制参数，如UE使用某个DNN可建立的最大PDU会话数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMPDUCTRL]] · PDU会话控制参数（SMPDUCTRL）

## 使用实例

查询AMF上当前配置的PDU会话管理参数，执行如下命令：

```
LST SMPDUCTRL:;
%%LST SMPDUCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
            DNN支持PDU会话数  =  15
     会话数量超DNN规格原因值  =  67
          网络切片无效原因值  =  90
               DNN无效原因值  =  91
           Back-off定时器(s)  =  0
               ODB拒绝原因值  =  0
            无签约数据原因值  =  8
SMF发现拒绝原因值(Not Found)  =  10
 SMF发现拒绝原因值(其他原因)  =  3
              是否校验SMF ID  =  关闭
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PDU会话控制参数（LST-SMPDUCTRL）_44007229.md`
