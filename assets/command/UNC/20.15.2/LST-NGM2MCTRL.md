---
id: UNC@20.15.2@MMLCommand@LST NGM2MCTRL
type: MMLCommand
name: LST NGM2MCTRL（查询5G M2M控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGM2MCTRL
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G M2M管理
- M2M控制参数
status: active
---

# LST NGM2MCTRL（查询5G M2M控制参数）

## 功能

**适用NF：AMF**

该命令用于查询5G M2M的控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGM2MCTRL]] · 5G M2M控制参数（NGM2MCTRL）

## 使用实例

查询5G M2M控制参数，执行如下命令：

```
%%LST NGM2MCTRL:;%%
RETCODE = 0  操作成功

结果如下
------------------------
             EDRX参数校正开关  =  是
           EDRX短周期使能开关  =  否
           NR模式寻呼窗口差值  =  时间相同
       可达性事件上报非标开关  =  否
AMF内移动性流程用户面建立优化  =  否
AMF间移动性流程用户面建立优化  =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G-M2M控制参数（LST-NGM2MCTRL）_34572336.md`
