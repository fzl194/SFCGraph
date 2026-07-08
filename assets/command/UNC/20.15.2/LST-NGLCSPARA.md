---
id: UNC@20.15.2@MMLCommand@LST NGLCSPARA
type: MMLCommand
name: LST NGLCSPARA（查询5G定位服务参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGLCSPARA
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 5G定位服务管理
- 定位服务管理
status: active
---

# LST NGLCSPARA（查询5G定位服务参数）

## 功能

**适用NF：AMF**

该命令用于查询AMF的定位服务功能的相关参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [5G定位服务参数（NGLCSPARA）](configobject/UNC/20.15.2/NGLCSPARA.md)

## 使用实例

查询5G定位服务的参数，执行如下命令：

```
%%LST NGLCSPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
           定位服务功能开关  =  关闭
5G位置信息表老化定时器(min)  =  60
             5G定位服务策略  =  协议模式定位
          启用连接态LRC流程  =  否
          是否携带GUAMI信息  =  否
 是否校验LCS Correlation ID  =  否
                是否重选LMF  =  否
               是否使用SUPI  =  否
               是否使用GPSI  =  否
           园区定位增强开关  =  关闭
          缺省的LMF群组标识  =  NULL
               是否使用切片  =  否
    是否携带lcsQosClass信息  =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G定位服务参数（LST-NGLCSPARA）_44007004.md`
