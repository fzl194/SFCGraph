---
id: UNC@20.15.2@MMLCommand@LST NSSELPARA
type: MMLCommand
name: LST NSSELPARA（查询网络切片选择相关参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSSELPARA
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 网络切片选择管理
- 网络切片选择控制参数
status: active
---

# LST NSSELPARA（查询网络切片选择相关参数）

## 功能

**适用NF：AMF**

该命令用于查询网络切片选择的相关参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSELPARA]] · 网络切片选择相关参数（NSSELPARA）

## 使用实例

查询网络切片选择的当前配置，执行如下命令：

```
%%LST NSSELPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
               同步开关  =  关闭
              间隔(min)  =  5
   自行决策能否为UE服务  =  是
       园区网络切片开关  =  关闭
        最大TAI切片数量  =  80000
         园区切片数据源  =  从NSSF获取
切片可用性流程GUAMI索引  =  256
   是否携带AMFSETID信息  =  否
       切片协商增强开关  =  打开
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NSSELPARA.md`
